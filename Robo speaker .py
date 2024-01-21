import os

print("WELCOME TO ROBO SPEAKER")

while True:
    Tell = input("Enter what you want to speak: ")
    command = f"PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{Tell}')"
    if Tell.lower() == "quit":
        print("ITS NICE TALKING WITH YOU")
        break  # Add a break statement to exit the loop when "quit" is entered
    else:
        os.system(command)
