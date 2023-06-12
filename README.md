# PlexNewContentGUI
Small GUI To send Discord Webhook embeds to a Discord server

GUI is mostly focused on Anime, but can easily be changed to any other need.

### Preview of the Script
![image](https://github.com/GhostTortilla/PlexNewContentGUI/assets/26606900/22ea7919-2d95-4f30-8068-34e042588b26)

## Field Descriptions
| Field | Description |
| :-: | --- |
| **Title** | Title Field which will be the "Header" of the Embed |
| **Image URL** | A URL to an image whic hwill be used as a thumbnail for the Embed |
| **Series URL** | A URL Which will be used as a clickable Header in the Embed |
| **Additional Notes** | SmalL Notes one can add which will be placed in the Footer of the Embed |
| **Dual Audio** | If Checked, the Audio Field in the Embed will be set to "Dual Audio" |
| **Subbed Only** | If Checked, the Audio Field in the Embed will be set to "Subbed Only" |
| **Is Movie** | If Checked, the Type Field in the Embed will be set to "Movie". This defaults to Anime. |
| **New/Updated** | Combobox with "New" / "Updated" choices. New is Default, and either will set the "New/Updated" Field to their respective Value. |
| **Episodes** | Usually an Int, but not restricted to numbers. Number of episodes etc. |
| **Seasons** | Usually an Int, but not restricted to numbers. Number of episodes etc. |

### Dependencies
* `customtkinter`
* `discord`
* `datetime`

```bash
pip install -r requirements.txt
```

### Running the Project
Switch out the WebHookURL with the one you want to use
```python
# Line 80
WebHookURL = "WebHookURL"
```
```bash
python main.py
```
