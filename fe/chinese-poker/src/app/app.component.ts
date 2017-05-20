import { Component, Input } from '@angular/core';
import { CardComponent } from './card/card.component';
import { DeckComponent, DEFAULT_DECK } from './deck/deck.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Chinese Poker';
  cards = DEFAULT_DECK;
}
