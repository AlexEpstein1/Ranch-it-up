import csv

def update_highscore(name, score):
	file_name = '../ReadWriteFiles/highscore.csv'
	highscorefile_read = open(file_name, "r")
	# Adding
	file_handler = csv.reader(highscorefile_read, delimiter=",")
	scores_array = []
	for row in file_handler:
		scores_array.append((row[0], int(row[1])))
	scores_array.append((name, score))
	organized_by_score_array = sorted(scores_array, key=lambda x: x[1])[::-1]
	organized_by_score_array = organized_by_score_array[0: 10]
	print(organized_by_score_array)
	highscorefile_read.close()

	highscorefile_write = open(file_name, 'w+')
	spamwriter = csv.writer(highscorefile_write, delimiter=',')
	for player_score in organized_by_score_array:
		spamwriter.writerow([player_score[0]] + [player_score[1]])
	highscorefile_write.close()
		
		

def main():
	update_highscore("Wesley", 1100)

main()