from . import DotGWriter

from UM.i18n import i18nCatalog
catalog = i18nCatalog("gwriter")

def getMetaData():
    return {
        "mesh_writer": {
            "output": [{
                "extension": "g",
                "description": catalog.i18nc("@item:inlistbox", "G File"),
                "mime_type": "text/x-dotg",
                "mode": DotGWriter.DotGWriter.OutputMode.TextMode
            }]
        }
    }

def register(app):
    return { "mesh_writer": DotGWriter.DotGWriter() }