import { Component, OnInit } from '@angular/core';
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

  constructor(deck: Deck) {
    super(deck.getCards());
  }

  ngOnInit() {
  }

}
