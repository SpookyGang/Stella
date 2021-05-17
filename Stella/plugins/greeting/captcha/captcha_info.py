__mod_name__ = "CAPTCHA"

__help__ = """
Some chats get a lot of users joining just to spam. This could be because they're trolls, or part of a spam network.
To slow them down, you could try enabling CAPTCHAs. New users joining your chat will be required to complete a test to confirm that they're real people.'

Admin commands:
- /captcha `<yes/no/on/off>`: All users that join will need to solve a CAPTCHA. This proves they aren't a bot!
- /captchamode `<button/math/text>`: Choose which CAPTCHA type to use for your chat.
- /captcharules `<yes/no/on/off>`: Require new users accept the rules before being able to speak in the chat.
- /captchatime `<Xw/d/h/m>`: Unmute new users after X time. If a user hasn't solved the CAPTCHA yet, they get automatically unmuted after this period.
- /captchakick `<yes/no/on/off>`: Kick users that haven't solved the CAPTCHA.
- /captchakicktime `<Xw/d/h/m>`: Set the time after which to kick CAPTCHA'd users.
- /setcaptchatext `<text>`: Customise the CAPTCHA button.
- /resetcaptchatext: Reset the CAPTCHA button to the default text.
- /recaptcha `<yes/no/on/off>`: Stella will ask the CAPTCHA to every new user, be it someone who has joined before and verified already

Examples:
- Enable CAPTCHAs
-> `/captcha on`
- Change the CAPTCHA mode to text.
-> `/captchamode text`
- Enable CAPTCHA rules, forcing users to read the rules before being allowed to speak.
-> `/captcharules on`

NOTE:
For CAPTCHAs to be enabled, you MUST have enabled welcome messages. If you disable welcome messages, CAPTCHAs will also stop.
"""