-- Presentation only: never rewrites the protected semantic QMD source.
local path = pandoc.path.join({pandoc.path.directory(PANDOC_SCRIPT_FILE), "goal-en.json"})
local handle = assert(io.open(path, "r"))
local translation = pandoc.json.decode(handle:read("*a"))
handle:close()

function Pandoc(doc)
  local found = false
  doc = doc:walk({
    Div = function(el)
      if el.identifier == translation.id then
        found = true
        el.attributes.name = translation.name
        el.content = pandoc.read(translation.statement_markdown, "markdown").blocks
        return el
      end
    end
  })
  if found and pandoc.utils.stringify(doc.meta.title) == "受保护中心定理" then
    doc.meta.title = pandoc.MetaInlines({pandoc.Str(translation.chapter_title)})
  end
  return doc
end
