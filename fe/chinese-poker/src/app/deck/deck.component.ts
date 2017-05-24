import { Component, OnInit, Input, Inject } from '@angular/core';
import { CardCollectionComponent } from '../card-collection/card-collection.component';
import { CardComponent } from '../card/card.component';
import { Card } from '../card/card';
import { Deck } from './deck';

@Component({
  selector: 'app-deck',
  templateUrl: './deck.component.html',
  styleUrls: ['./deck.component.css']
})
export class DeckComponent extends CardCollectionComponent implements OnInit {

  @Input protected cards: Deck;

  constructor(@Inject('cards') protected cards: Deck) {
    super(cards);
  }

  ngOnInit() {
  }

}
