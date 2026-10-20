-- Resolve the report's repository-local evidence links against its immutable input snapshot.
local base = 'https://github.com/aaaaaaaaaaaavm/VOLLEY-thesis/blob/24804907b30c9f0e568c134eb3a90269ec3caec5/'
function Link(el)
  if el.target:match('^%.%./') then el.target=base..el.target:gsub('^%.%./','') end
  return el
end
function RawBlock(el)
  if FORMAT=='docx' and el.format=='tex' and el.text:match('\\clearpage') then
    return pandoc.RawBlock('openxml','<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
  end
end
local figure_number=0
local table_number=0
local function caption_prefix(caption,label)
  if #caption.long>0 and caption.long[1].content then
    table.insert(caption.long[1].content,1,pandoc.Str(label..':'))
    table.insert(caption.long[1].content,2,pandoc.Space())
  end
end
function Figure(el)
  if FORMAT=='docx' then figure_number=figure_number+1;caption_prefix(el.caption,'Figure '..figure_number) end
  return el
end
function Table(el)
  if FORMAT=='docx' then table_number=table_number+1;caption_prefix(el.caption,'Table '..table_number) end
  return el
end
