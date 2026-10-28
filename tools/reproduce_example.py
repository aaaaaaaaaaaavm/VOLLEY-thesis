#!/usr/bin/env python3
"""Reproduce real ACR1 logic, sizing and one source-coupled shot in a scratch copy."""
from pathlib import Path
import contextlib,importlib.util,io,json,runpy,shutil,sys,tempfile
R=Path(__file__).resolve().parents[1]
def module(path):
 spec=importlib.util.spec_from_file_location('acr1_example',path);m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);return m
with tempfile.TemporaryDirectory(prefix='volley-acr1-example-') as d:
 C=Path(d)/'current'
 # Copy only the actual inputs used below, preserving their relative paths.
 # The full distribution also contains CAD binaries and solver archives that
 # are not required for this numerical example.
 required=(
  'analysis/transfer_interlocks.py','analysis/feeder_sizing.py',
  'analysis/FEEDER_SIZING.json','analysis/coupled_shot.py',
  'analysis/COUPLED_SHOT.json','analysis/FINITE_MOTOR.json',
  'analysis/ARREST_FORCE_MAP.json','analysis/conduction/phase_A/h2/RESULT.json',
  'cad/PARAMETERS.json','cad/release/VOLLEY_G5_ACR1_home.json',
  'sources/feeder_catalog_reference.json',
 )
 for relative in required:
  destination=C/relative;destination.parent.mkdir(parents=True,exist_ok=True)
  shutil.copyfile(R/'current'/relative,destination)
 runpy.run_path(str(C/'analysis/transfer_interlocks.py'),run_name='__main__')
 logic=json.loads((C/'analysis/TRANSFER_INTERLOCKS.json').read_text())
 assert logic['accepted_nominal_commands']==24 and logic['tests']==166 and logic['all_passed']
 m=module(C/'analysis/feeder_sizing.py')
 with contextlib.redirect_stdout(io.StringIO()):m.calculate()
 result=json.loads((C/'analysis/FEEDER_SIZING.json').read_text())
 captured=json.loads((R/'current/analysis/FEEDER_SIZING.json').read_text())
 assert result==captured,'Feeder result differs from controlled capture'
 shot=module(C/'analysis/coupled_shot.py');sled,dry,xs,ks,resistance,hashes=shot.inputs()
 reference=json.loads((C/'analysis/COUPLED_SHOT.json').read_text())
 assert hashes==reference['inputs_sha256']
 expected=next(c for c in reference['cases'] if c['target_m_s']==3 and not c['adverse'] and c['inductance_H']==2e-5)
 actual=shot.simulate(3,sled,dry,xs,ks,resistance,adverse=False,L=2e-5,dt=2e-5)
 assert actual['status']=='STOPPED' and actual['all_declared_checks_pass']
 for key in ['stop_position_m','peak_phase_current_A']:
  assert abs(actual[key]-expected[key])<1e-8,(key,actual[key],expected[key])
 assert abs(actual['release']['relative_speed_m_s']-expected['release']['relative_speed_m_s'])<1e-10
 print(json.dumps({'configuration':'VOLLEY-G5-ACR1','logic_tests':logic['tests'],'feeder_matches_capture':True,'shot_target_m_s':3,'release_speed_m_s':actual['release']['relative_speed_m_s'],'arrest_position_m':actual['stop_position_m'],'all_declared_shot_checks_pass':True},indent=2))
