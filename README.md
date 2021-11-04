# FlashForge-Creator-Pro-2-Cura
### Installation:

1. Copy the 'scripts' folder to your Cura Configuration Folder. You can find this under 'Help > Show Configuration Folder'
2. Copy each section of G code from 'Machine Settings' and paste into the corresponding sections in your cura machine settings for the Creator Pro 2
3. Open Cura and drag the .curapackage file directly onto the Cura window
4. To set '.g' as the default for saving gcode, add `file_formats = text/x-dotg` under `[metadata]` for each printer's setting file in your Configuration Folder's definition_changes

### Possible scripts/plugins for the future:

- Automatically disabling one extruder to avoid switching machine settings for single extruder prints

- include print preview used in .gx files

### Credit to:
- [This reddit post](https://www.reddit.com/r/FlashForge/comments/oq4twg/using_cura_with_flashforge_creator_pro_2) for the Creator Pro 2 machine settings
