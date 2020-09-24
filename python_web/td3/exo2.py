import re

phrase = 'le python est un serpent sympathique qui aime la salade'
print(re.match('(.*) est (.*) qui (.*)', phrase).groups())