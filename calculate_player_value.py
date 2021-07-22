import pickle, itertools
from file_path_converter import convert_path

pi = True

team = 'Arsenal'
player_name = 'Alexandre Lacazette'

team_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\'+team+'.dat'
if pi :
	team_path = convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\'+team+'.dat')

loaded = pickle.load(open(team_path, 'rb'))

			
#def calculate_value() :
	
