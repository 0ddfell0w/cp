import { Component, Input } from '@angular/core';
import { CardComponent } from './card/card.component';
import { DeckComponent } from './deck/deck.component';
import { Deck, DEFAULT_DECK } from './deck/deck';
import { CardCollection } from './card-collection/card-collection';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Chinese Poker';
  deck : CardCollection = DEFAULT_DECK;
}
