from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkSwitch, CTkComboBox
from discord import SyncWebhook, Embed
from datetime import datetime

class App(CTk):

    def __init__(self):
        CTk.__init__(self)
        CTk._set_appearance_mode(self, "dark")
        CTk.title(self, "Plex New Content")
        CTk.geometry(self, "750x500")
        CTk.resizable(self, False, False)
        ### Create the Layout ###
        self.Layout()

    def Layout(self):
        ### Title Label & Entry Box ###
        self.TitleLabel = CTkLabel(self, text="Title", font=("ComicSansMS", 25))
        self.TitleLabel.place(relx=0.5, rely=0.05, anchor="center")
        self.TitleInputBox = CTkEntry(self, height=0.75, width=650, font=("ComicSansMS", 15), text_color="white", justify="center", placeholder_text="Enter the title")
        self.TitleInputBox.place(relx = 0.5, rely = 0.115, anchor = "center")

        ### Image URL Label & Entry Box ###
        self.ImageURLLabel = CTkLabel(self, text="Image URL", font=("ComicSansMS", 25))
        self.ImageURLLabel.place(relx=0.5, rely=0.2, anchor="center")
        self.ImageURLInputBox = CTkEntry(self, height=0.75, width=650, font=("ComicSansMS", 15), text_color="white", justify="center", placeholder_text="URL for the Embed Thumbnail")
        self.ImageURLInputBox.place(relx=0.5, rely=0.265, anchor="center")

        ### Series URL Label & Entry Box ###
        self.SeriesURLLabel = CTkLabel(self, text="Series URL", font=("ComicSansMS", 25))
        self.SeriesURLLabel.place(relx=0.5, rely=0.35, anchor="center")
        self.SeriesURLInputBox = CTkEntry(self, height=0.75, width=650, font=("ComicSansMS", 15), text_color="white", justify="center", placeholder_text="Clickable URL for the Embed Title")
        self.SeriesURLInputBox.place(relx = 0.5, rely = 0.415, anchor = "center")
        
        ### Additional Notes Label & Entry Box ###
        self.NotesLabel = CTkLabel(self, text="Additional Notes", font=("ComicSansMS", 25))
        self.NotesLabel.place(relx=0.5, rely=0.5, anchor="center")
        self.NotesInputBox = CTkEntry(self, height=0.75, width=650, font=("ComicSansMS", 15), text_color="white", justify="center", placeholder_text="Additional text which will be placed in the Embeds Footer.")
        self.NotesInputBox.place(relx=0.5, rely=0.565, anchor="center")

        ### Dual Audio Radio Button ###
        self.DualAudioCheck = CTkSwitch(self, text="Dual Audio", font=("ComicSansMS", 15, "bold"), text_color="white")
        self.DualAudioCheck.place(relx=0.15, rely=0.65)
        
        ### Subbed Only Radio Button ###
        self.SubbedCheck = CTkSwitch(self, text="Subbed", font=("ComicSansMS", 15, "bold"), text_color="white")
        self.SubbedCheck.place(relx=0.15, rely=0.75)
        
        ### Is Movie Check Box ###
        self.IsMovieCheck = CTkSwitch(self, text="Is Movie", font=("ComicSansMS", 15, "bold"), text_color="white")
        self.IsMovieCheck.place(relx=0.15, rely=0.85)
        
        ### New/Updated Label & ComboBox ###
        self.NewOrUpdatedLabel = CTkLabel(self, text="New / Updated", font=("ComicSansMS", 15, "bold"))
        self.NewOrUpdatedLabel.place(relx=0.737, rely=0.62)
        self.NewOrUpdated = CTkComboBox(self, values=["New", "Updated"], font=("ComicSansMS", 15), text_color="white")
        self.NewOrUpdated.place(relx=0.8, rely=0.7, anchor="center")

        ### Episode Label & Entry Box ###
        self.EpisodesLabel = CTkLabel(self, text="Episodes", font=("ComicSansMS", 15, "bold"))
        self.EpisodesLabel.place(relx=0.645, rely=0.82)
        self.Episodes = CTkEntry(self, height=0.75, width=80, font=("ComicSansMS", 15), text_color="white", justify="center")
        self.Episodes.place(relx=0.635, rely=0.87)

        ### Season Label & Entry Box ###
        self.SeasonsLabel = CTkLabel(self, text="Seasons", font=("ComicSansMS", 15, "bold"))
        self.SeasonsLabel.place(relx=0.845, rely=0.82)
        self.Seasons = CTkEntry(self, height=0.75, width=80, font=("ComicSansMS", 15), text_color="white", justify="center")
        self.Seasons.place(relx=0.835, rely=0.87)

        ### Send Button ###
        self.SendButton = CTkButton(self, text="Send", font =("ComicSansMS", 25), command=self.SendMessage, hover_color="green")
        self.SendButton.place(relx=0.5, rely=0.75, anchor="center")

        ### Exit Button ###
        self.ExitProgram = CTkButton(self, text="Exit", command=self.destroy, hover_color="red")
        self.ExitProgram.place(relx=0.5, rely=0.95, anchor="center")


    def SendMessage(self):
        WebHookURL = "WebHookURL"
        WebHook = SyncWebhook.from_url(WebHookURL)
        
        ### Get the Button/Switch Values ###
        if self.DualAudioCheck.get():
            Audio = "Dual Audio"
        elif self.SubbedCheck.get():
            Audio = "Subbed Only"
        else:
            Audio = "None"

        if self.IsMovieCheck.get():
            Type = "Movie"
        else:
            Type = "Anime"
        
        ### Create the Embed ###
        Data = Embed()
        Data.title = self.TitleInputBox.get()
        Data.add_field(name="Audio", value=Audio)
        Data.add_field(name="Date Added", value=datetime.today().strftime('%d-%m-%Y'))
        Data.add_field(name="Type", value=Type)
        Data.add_field(name="New/Updated", value=self.NewOrUpdated.get())
        Data.add_field(name="Season(s)", value=self.Seasons.get())
        Data.add_field(name="Episodes", value=self.Episodes.get())
        Data.url = self.SeriesURLInputBox.get()
        Data.set_thumbnail(url = self.ImageURLInputBox.get())
        Notes = self.NotesInputBox.get()
        if Notes:
            Data.set_footer(text=f"Additional Notes: {Notes}")
          
        ### Send the Embed ###
        WebHook.send(embed=Data)

if __name__ == "__main__":
    App().mainloop()
