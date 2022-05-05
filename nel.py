#Nel is a caretaker who is in charge of the Kaya,There are curtains surrounding kaya,
# if the clouds appear rainy,instruct Kili,your smart device to close the curtains,if it
#has stopped raining instruct Kili to draw the curtains.
from tracemalloc import stop


print('Kili is a smart device that opens and closes the curtains depending on weather of the day')
answer=str((input("Enter yes if you want to draw curtains with Kili's help")))
if answer =='yes':
    print('am glad to work with you')
elif answer =='no':
    stop
a=str(input("Enter the weather"))
weather='it is rainy' or 'it is calm'
b='ssob sniatruc gniward'
c='ssob ereh doog lla era ew'
if weather =='it is rainy':
    print(b[::-1])
elif weather=='it is calm':
    print(c[::-1])
