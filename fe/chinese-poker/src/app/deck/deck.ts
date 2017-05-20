import { CardCollection } from '../card-collection/card-collection';
import { Card } from '../card/card';

export class Deck extends CardCollection {

  constructor (cards: Array<Card>) {
    super(cards);
  }

  getCards(): Array<Card> {
    return this.cards;
  }

  popCard(): Card {
    return this.cards.pop();
  }

  addCard(card: Card): number {
    this.cards.push(card);
    return this.cards.length;
  }

  contains(rank: string, suit: string) : boolean {
    for (let card of this.cards) {
      if (card.rank === rank && card.suit === suit) {
        return true;
      }
    }
    return false;
  }
}


export const DEFAULT_DECK: Deck = (function() : Deck {
  return new Deck([
    new Card("3", "D"),
    new Card("3", "C"),
    new Card("3", "H"),
    new Card("3", "S"),
    new Card("4", "D"),
    new Card("4", "C"),
    new Card("4", "H"),
    new Card("4", "S"),
    new Card("5", "D"),
    new Card("5", "C"),
    new Card("5", "H"),
    new Card("5", "S"),
    new Card("6", "D"),
    new Card("6", "C"),
    new Card("6", "H"),
    new Card("6", "S"),
    new Card("7", "D"),
    new Card("7", "C"),
    new Card("7", "H"),
    new Card("7", "S"),
    new Card("8", "D"),
    new Card("8", "C"),
    new Card("8", "H"),
    new Card("8", "S"),
    new Card("9", "D"),
    new Card("9", "C"),
    new Card("9", "H"),
    new Card("9", "S"),
    new Card("10", "D"),
    new Card("10", "C"),
    new Card("10", "H"),
    new Card("10", "S"),
    new Card("J", "D"),
    new Card("J", "C"),
    new Card("J", "H"),
    new Card("J", "S"),
    new Card("Q", "D"),
    new Card("Q", "C"),
    new Card("Q", "H"),
    new Card("Q", "S"),
    new Card("K", "D"),
    new Card("K", "C"),
    new Card("K", "H"),
    new Card("K", "S"),
    new Card("A", "D"),
    new Card("A", "C"),
    new Card("A", "H"),
    new Card("A", "S"),
    new Card("2", "D"),
    new Card("2", "C"),
    new Card("2", "H"),
    new Card("2", "S")
  ]);
})();
