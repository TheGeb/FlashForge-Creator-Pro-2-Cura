# FlashForge-Creator-Pro-2-Cura
### Installation:

1. Copy the 'scripts' folder to your Cura Configuration Folder. You can find this under 'Help > Show Configuration Folder'
2. Copy each section of G code from 'Machine Settings' and paste into the corresponding sections in your cura machine settings for the Creator Pro 2
3. Download the plugin that you'd like from the links below
4. To set '.gx' as the default for saving gcode, add `file_formats = application/gx` under `[metadata]` for each printer's setting file in your Configuration Folder's definition_changes. If you would prefer .g, use `file_formats = text/x-dotg`

### Plugins:

| file extension | file format      | plugin link |
| -------------- | ---------------- | ----------- |
| .gx            | `application/gx` | https://marketplace.ultimaker.com/app/cura/plugins/Ronoaldo/GXWriter  |
| .g             | `text/x-dotg`    | https://marketplace.ultimaker.com/app/cura/plugins/gebfred/DotGWriter |

### Possible scripts/plugins for the future:

- Automatically disabling one extruder to avoid switching machine settings for single extruder prints

### Credit to:
- [This reddit post](https://www.reddit.com/r/FlashForge/comments/oq4twg/using_cura_with_flashforge_creator_pro_2) for the Creator Pro 2 machine settings
