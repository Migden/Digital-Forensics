import subprocess

class HistoryAnalyzer:
	def __init__(self, Path, HistoryLocation='History'):
		self.Path=Path
		self.HistoryLocation=HistoryLocation
		self.Content=""		
		self.URLs=[]
		self.SetPathToHistory()
		self.ReadInformation()
		self.ReturnURLs()
		self.Return()
	
	def SetPathToHistory(self):
		self.Path+=f"/{self.HistoryLocation}"

	def ReadInformation(self):
		f = open(self.Path, 'r+b')
		self.Content=f.read()

	def ReturnURLs(self):
		PrivateContentURLsAnalyze=str(self.Content).split('http')
		for i in range(0, len(PrivateContentURLsAnalyze)):
			if PrivateContentURLsAnalyze[i][0] == 's' or PrivateContentURLsAnalyze[i][0] == ':':
				self.URLs.append(f"http{PrivateContentURLsAnalyze[i]}")

	def Return(self):
		return(self.URLs)

def main(Path):
	Analysis=HistoryAnalyzer(ChromeDefaultPath)

if __name__ == "__main__":
	User=subprocess.check_output('whoami').decode('utf-8').strip().split("\\")
	ChromeDefaultPath=f"C:/Users/{User[1]}/AppData/Local/Google/Chrome/User Data/Default"
	main(ChromeDefaultPath)
