
# Application_Verification

Verify Applications using a duplicate of the Sourcecode
---

<br>

To use this script you need to create a github repository,

then create a file and insert the link to your unmodified

program (The user might be able to see the link).

Then copy the raw link (Save the file and press the Raw button)

The link should look something like this:

"`https://raw.githubusercontent.com/########/################/main/########`"

Add the url to the `CLIENT\check.py` in the `GITHUB_URL_OVERWRITE_RAW_URL` variable at the top

Then just compile the script using whatever tool you want to use and run it at the start of your application
