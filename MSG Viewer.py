# Feel Free to Modify and Play with the code
# Main Contributor: ChatGPT 3.5
# GIT BUILD 0.1 (Alpha)

'''
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&%%%%&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&%%%%%&&&&%&&&&&&&%%&&%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%&%%&&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%&&&&&&&&&&&&%%%%%%%%%&&&&&&%&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%&&&&&&&&&&&&&&%%%%%%%%%%&%%&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%&&%&&%%&&&%%%%%%%%%%%%%%%%%%%&&%%%%%%%&%&&&&&&&&&&&%%%%%%%%%%%%%%%
%%%%%%%%%%%%&&&&%&&&%%&&#//,,,,,,,*/&#/**/%%#&*......,*%&&&%&&&&&%%%%%%%%%%%%%%%
%%%%%%%%%%%&&&&&&%&&&#**,,,.,,,,,../,......,*. #.......,(%&%&&&&%%%%%%%%%%%%%%%%
%%%%%%%%%%%&&&&&&&%%#**,,,,,,,,,,,.......................#%&%&&&%%%%%%%%%%%%%%%%
%%%%%%%%%%%&&&&&&&%&/*,,,,,,,,,,..........................%%&&&&%%%%%%%%%%%%%%%%
%%%%%%%%%%%%&&&&&&&&(/,,,,,,,,,...........................(&&&&&%%%%%%%%%%%%%%%%
%%%%%%%%%%%%&&&&&%&%#/,,,,,,,,............................(&&&%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%&&&&&%%/,,,*#####%%%#/.......*#%%%#####*....(&&%%%%%%%%%%%%%%%%%%%  
%%%%%%%%%%%%%%&&&%&%&(,,,#(##########%,,,%############*.. %%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%&&&&#,,,(########(##*...*###########(...,@&%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%&#.,.,.*####(###*.....*#(######/.....#%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%&(.,................................*&%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%@............., ..... ,........... #%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%&(..............,...,............./&%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%&&(........,(%&&&&%%&&&&(,........@%%%%%%%%%%%%%%%%%%%%%%%% poda andha aandavane namma pakkam!!!
%%%%%%%%%%%%%%%%%%%%%&&&&*,....%&&(........./&%%,,..,(&&&%%&%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%&&&&&&@,......(%&&%&%&.......*&&&%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%&&(&&%%&&,....%&%%%&%%&&*....,%%&&#,&%%&%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%&&#   (&%%&%%%&%%&%%&&&&&&&&%&&&%&&, . (@&%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%&%    .*#%&%&%&%&%&%&%%&&&&%&%&&%%#,     .%&%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%&&&%.      .(%##%&&&&&&&&&&&&&&&&%&%##.        .%&&%&%%%%%%%%%%%%%%
%%%%%%%%%%%%&&&&*       **.#################%##(#*  *&       *&&&&%%%%%%%%%%%%%%
%%%%%%%%%%&&&&&&&&&&*   %%#. (#################*   %%@.  *%@&&&&&&&&%%%%%%%%%%%%
%%%%%%%%%%%%%&&&&&&&&&#.@&%%. .###############.   (%&&/#&&&&&&&&&%%%%%%%%%%%%%%%
%%%%%%%%%%&&&&&&&&&&&&&&&&&%%/   .(#########/    *%&&&&&&&&&&&&&&&&%%%%%%%%%%%%%
%%%%%%%%%&&&&&&&&&&&&&&&&&&%%#%,   /######%,    ##%&&&&&&&&&&&&&&&&&&%%%%%%%%%%%
%%%%%%%%%%&&&&&&&&&&&&&&&&&%%%%%,   &#####*  .(%%%&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%
%%%%%%%%%%%&&&&&&&&&&&&&&&&&#%##%/  .%#### .#%###%&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%
%%%%%%%%%%%%%&&&&&&&&&&&&&&&&%%%%%%/  ##%.,&%%%%#&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%
%%%%%%%%%%%%%&&&&&&&&&&&&&&&&%%%%%%#&. *,.%%%%%%%&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%&&&&&&&&&&&&&&%%%%%#%%%   %%%%%%%&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&%%%%%%%%%(#%%%%%%%&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%&&%%&&&&&&&&&&&&&&%%%%%%%%%%%%%%%#&&&&&&&&&&&&&%%%&&%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&%%%%%%%%%%%%%%%%&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%

'''




import os
import tkinter as tk
from tkinter import filedialog
from extract_msg import Message

def view_message_content():
    # Open a file dialog to select the .msg file
    file_path = filedialog.askopenfilename(filetypes=[("Email Files", "*.msg")])

    if file_path:
        # Split the Message File into File Name and Extension
        _, file_extension = os.path.splitext(file_path)

        if file_extension.lower() == ".msg":
            # Parse the .msg file
            msg = Message(file_path)

            # Get the subject and body of the email
            subject = msg.subject
            body = extract_email_body(msg)

            # Create a new Tkinter window to display the content
            content_window = tk.Toplevel(root)
            content_window.title("Message Content")

            # Create a scrollable text widget to show the subject and body
            text_widget = tk.Text(content_window, wrap="word")
            text_widget.insert("1.0", f"Subject: {subject}\n\n{body}")
            text_widget.pack(expand=True, fill="both")

            # Create a vertical scrollbar and associate it with the text widget
            scroll_bar = tk.Scrollbar(content_window, command=text_widget.yview)
            scroll_bar.pack(side="right", fill="y")

            # Configure the text widget to use the scrollbar
            text_widget.config(yscrollcommand=scroll_bar.set)

            # Save attachments to desktop
            save_attachments_to_desktop(file_path, msg.attachments)

def extract_email_body(msg):
    # Get the body of the email
    body = msg.body

    # If the body is not in plain text, use the HTML body if available
    if not body:
        body = msg.htmlBody

    return body

def save_attachments_to_desktop(file_path, attachments):
    # Get the desktop path
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    # Create a folder with the same name as the .msg file on the desktop
    file_name = os.path.basename(file_path)
    folder_name = os.path.splitext(file_name)[0]
    folder_path = os.path.join(desktop_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Save attachments to the folder on the desktop
    
    for attachment in attachments:
        attachment_path = os.path.join(folder_path, attachment.longFilename)
        with open(attachment_path, 'wb') as f:
            f.write(attachment.data)
            


if __name__ == "__main__":
    # Create the main tkinter window
    root = tk.Tk()
    root.title("MSG VIEWER")

    # Create a button to open the file dialog
    open_button = tk.Button(root, text="Open MSG Files", command=view_message_content)
    open_button.pack()

    # Start the Tkinter main loop
    root.mainloop()




"""
ORIGINAL IDEA 
        |
        |
        |
        V

import extract_msg

f = r'Test.msg'  # Replace with your name of the msg file
msg = extract_msg.Message(f)
msg_sender = msg.sender
msg_date = msg.date
msg_subj = msg.subject
msg_message = msg.body

print('Sender: {}'.format(msg_sender))
print('Sent On: {}'.format(msg_date))
print('Subject: {}'.format(msg_subj))
print('Body: {}'.format(msg_message))

"""