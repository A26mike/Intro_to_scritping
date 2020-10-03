import re

#Paragraph provided for search and replace

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''


search_string = '[\W]' # seach all non numarical chars same as[^a-zA-Z0-9_]
results = re.findall(search_string, lorem_ipsum)
print(len(results))

#count occurance of sit[-:]amet
pattern = 'sit[-:]amet'
occurrance_sit_amet = re.findall(pattern, lorem_ipsum)
print(len(occurrance_sit_amet))

#replace sit:amet and sit-amet with sit amet
pattern = 'sit[-:]amet'
substitution = 'sit amet'
replace_results = re.sub(pattern, substitution, lorem_ipsum)
#check if it worked correctly 
occurrence_sit_amet = re.findall(substitution,replace_results)
print(len(occurrence_sit_amet))