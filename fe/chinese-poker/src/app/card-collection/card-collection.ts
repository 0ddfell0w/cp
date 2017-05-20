import { Card } from '../card/card';

export abstract class CardCollection {

  constructor(protected cards: Array<Card>) {}

  abstract getCards(): Array<Card>;

  abstract popCard(): Card;

  abstract addCard(card: Card): number;

  abstract contains(rank: string, suit:string): boolean;
}
