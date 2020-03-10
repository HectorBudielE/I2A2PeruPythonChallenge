[//]: # (Image References)

[image1]: ./encoding.png "Sample Output"


# Solution Description

The solution for this challenge was based on the [Cactus Kev's Poker Hand Evaluator algorithm](http://suffe.cool/poker/evaluator.html).This algorithm can be explained in the following way:

1. There are C(52,5) or 2,598,960 possible unique poker hands. However, there are only 7462 distinct poker hand values.

2. A method was necessary to help the algorithm be order independent (mixing up the five cards does not change the overall value of the hand). Assigning a prime number value to each of the thirteen card ranks would result in an unique product per poker hand, regardless of the order of the five cards. That was the chosen method to deal with the order independence.

3. An encoding for each card is necessary to make comparisons and to contain all the necessary information. The chosen encoding was the following:

![Sample Output][image1]

4. Once encoded, each card could be used to filter the hand types and values. First, if the suits of the five cards are equal, then we have either a Flush or a Straight Flush. A bitwise operation is used (card1 AND card2 AND card3 AND card4 AND card5 AND 0xF000) to check this equality. Then, a lookup table (the <em>flushes</em> table) is used to check the hand value with the bit value of the cards (bitwise operation: (card1 OR card2 OR card3 OR card4 OR card5)>>16).

5. If the hand is not a Flush or a Straight Flush, then it could be a Straight or a High Card hand. The bit value of the cards used in the previous step can be used with another lookup table (the <em>unique5</em> table) for the Straight and High Cards, to check the hand value of these hands.

6. So far, 2574 out of the 7462 possible distinct hand values have been eliminated.

7. With the rest of the hand values, the prime product was used to differentiate between hands and to calculate their value (by searching the prime product in the product table <em>products</em> with binary search, to then use the index of the found prime product to get the hand value in the <em>values</em> table)

8. Once the algorithm for calculating the poker hand value was implemented, a class was specified to represent each Poker hand, including a method to compare one poker hand with another.

9. The program was tested using a unittest file, included inside this repo.