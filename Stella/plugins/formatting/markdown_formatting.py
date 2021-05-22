#    Stella (Development)
#    Copyright (C) 2021 - meanii (Anil Chauhan)
#    Copyright (C) 2021 - SpookyGang (Neel Verma, Anil Chauhan)

#    This program is free software; you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by 
#    the Free Software Foundation; either version 3 of the License, or 
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


__mod_name__ = "Markdown Formatting"

__hidden__ = True 

__help__ = """
You can format your message using bold, italics, underline, and much more. Go ahead and experiment!

**Supported markdown:**
- `code words: Backticks are used for monospace fonts. Shows as: code words.
- _italic words_: Underscores are used for italic fonts. Shows as: italic words.
- *bold words*: Asterisks are used for bold fonts. Shows as: bold words.
- ~strikethrough~: Tildes are used for strikethrough. Shows as: strikethrough.
- __underline__: Double underscores are used for underlines. Shows as: underline. NOTE: Some clients try to be smart and interpret it as italic. In that case, try to use your app's built-in formatting.
- [hyperlink](github.com): This is the formatting used for hyperlinks. Shows as: hyperlink.
- [My button](buttonurl://github.com): This is the formatting used for creating buttons. This example will create a button named "My button" which opens github.com when clicked.
If you would like to send buttons on the same row, use the :same formatting. EG:
[button 1](buttonurl://example.com)
[button 2](buttonurl://example.com:same)
[button 3](buttonurl://example.com)
This will show button 1 and 2 on the same line, with 3 underneath.
"""
