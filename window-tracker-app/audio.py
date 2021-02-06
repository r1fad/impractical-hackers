from google.cloud import texttospeech
from playsound import playsound
import time 
import html

# run export GOOGLE_APPLICATION_CREDENTIALS="impractical-hackers-ce3c2d8b1bea.json"

taunts = {
    1: "Stop browsing {}.",
    2: "Get back to work. Browse {} later.",
    3: "Ok honestly, you need to get back to work. {} will not pay the bills.",
    4: "Seriously, you are getting on my nerves. You need to stop this right now.",
    5: "Your machine will self destruct in 5. 4. 3. 2. 1.",
    6: "Wow. {} is more important than your own life. I see how it is.",
    7: "I give up. You clearly do not care."
}

MAX_PROMPTS = len(taunts)

def text_to_ssml(raw_lines):
    # Generates SSML text from plaintext.
    # Given an input filename, this function converts the contents of the text
    # file into a string of formatted SSML text. This function formats the SSML
    # string so that, when synthesized, the synthetic audio will pause for two
    # seconds between each line of the text file. This function also handles
    # special text characters which might interfere with SSML commands.
    #
    # Args:
    # inputfile: string name of plaintext file
    #
    # Returns:
    # A string of SSML text based on plaintext input

    # Replace special characters with HTML Ampersand Character Codes
    # These Codes prevent the API from confusing text with
    # SSML commands
    # For example, '<' --> '&lt;' and '&' --> '&amp;'

    escaped_lines = html.escape(raw_lines)

    # Convert plaintext to SSML
    # Wait two seconds between each address
    ssml = "<speak>{}</speak>".format(
        escaped_lines.replace(".", '<break time="0.5s"/>')
    )

    # Return the concatenated string of ssml script
    return ssml

# Instantiates a client
client = texttospeech.TextToSpeechClient()

def play_audio(prompts, app="facebook"):

  if prompts > MAX_PROMPTS:
    return

  # Set the text input to be synthesized
  text_to_say = text_to_ssml(taunts.get(prompts).format(app))
  synthesis_input = texttospeech.SynthesisInput(ssml=text_to_say)

  # Build the voice request, select the language code ("en-US") and the ssml
  # voice gender ("neutral")
  voice = texttospeech.VoiceSelectionParams(
      language_code="en-UK", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
  )

  # Select the type of audio file you want returned
  audio_config = texttospeech.AudioConfig(
      audio_encoding=texttospeech.AudioEncoding.MP3
  )

  # Perform the text-to-speech request on the text input with the selected
  # voice parameters and audio file type
  response = client.synthesize_speech(
      input=synthesis_input, voice=voice, audio_config=audio_config
  )

  # The response's audio_content is binary.
  with open("output.mp3", "wb") as out:
      # Write the response to the output file.
      out.write(response.audio_content)

  playsound("output.mp3")

if __name__ == "__main__":
  for i in range(1, 8):
      play_audio(i, "netflix")
      time.sleep(1)