# FlashForge-Creator-Pro-2-Cura
### Installation:

1. Copy the contents of each file in "resources/" to its corresponding Cura Configuration Folder. You may need to create some of the folders. You can find the configuration folder in Cura with 'Help > Show Configuration Folder'
2. Download the GXWriter plugin from the link below
3. Launch Cura and add the "Creator Pro 2" printer
4. Go to "Extensions -> Post Processing -> Modify G-Code", then select "Creator Pro 2 Temperature Fix" to ensure temperatures are correctly applied in dual-extrusion modes

### Prerequisite .GX File Plugin:

| file extension | file format      | Cura marketplace | source code |
| -------------- | ---------------- | ---------------- | ----------- |
| .gx            | `application/gx` | [GXWriter plugin](https://marketplace.ultimaker.com/app/cura/plugins/Ronoaldo/GXWriter) | [GXWriter github](https://github.com/ronoaldo/FlashforgeFinderIntegration/tree/master/plugins/GXWriter) |

Note:
"Relative Extrusion" does not appear to be supported by the Creator Pro 2. Ensure this is unchecked for all of your print profiles. You can find this setting under "Print Settings" -> "Special Modes"

### Credit to:
- [This reddit post](https://www.reddit.com/r/FlashForge/comments/oq4twg/using_cura_with_flashforge_creator_pro_2) for the Creator Pro 2 machine settings
- [This github repo](https://github.com/eugr/Flashforge-for-Cura/tree/master) which provided the platform mesh and definition files which I used as a template
