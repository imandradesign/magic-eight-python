import random
import time


def get_fortune(i):
    if i == 1:
        fortune = 'Probably, maybe?'
    if i == 2:
        fortune = 'Almost certainly!'
    if i == 3:
        fortune = "I guess you'll just have to find out the slow way like the rest of us."
    if i == 4:
        fortune = 'Could be. Could be...'
    if i == 5:
        fortune = "I feel like you should embrace the mystery in life. Because you're not going to like the answer..."
    if i == 6:
        fortune = "It's definitely possible, but no."
    if i == 7:
        fortune = "Odds are in your favor! But they're odds, so it could still be no."
    elif i == 8:
        fortune = 'Answer cloudy, try again later.'

    return fortune


def think_mystic_thoughts():
    wait = random.randint(1, 10)
    start = 0

    print('thinking....')

    while start < wait:
        print('.' * random.randint(1, 15))
        time.sleep(1)
        start += 1


def main():
    question = input('What is your question?\n\t> ')

    if '?' in question[-1]:
        i = random.randint(1, 8)
        fortune = get_fortune(i)

        print('The magic 8 ball sees all!')
        think_mystic_thoughts()
        print("You asked: " + question)
        print('Your fortune is: ' + fortune)

    else:
        print("It looks like that wasn't a question. Please ask a proper question!")
        main()


if __name__ == '__main__':
    main()
