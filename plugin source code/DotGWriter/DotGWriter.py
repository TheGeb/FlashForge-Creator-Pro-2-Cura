from UM.Mesh.MeshWriter import MeshWriter
import UM.PluginRegistry

from UM.i18n import i18nCatalog
catalog = i18nCatalog("gwriter")


class DotGWriter(MeshWriter):

    def write(self, stream, nodes, mode = MeshWriter.OutputMode.TextMode):
        gWriter = UM.PluginRegistry.PluginRegistry.getInstance().getPluginObject("GCodeWriter")
        return gWriter.write(stream, nodes, mode)
