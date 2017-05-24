import { Component, Inject, OnInit, Input } from '@angular/core';
import { Card } from '../card/card';
import { CardCollection } from '../card-collection/card-collection';

@Component({
  selector: 'app-card-collection',
  templateUrl: './card-collection.component.html',
  styleUrls: ['./card-collection.component.css']
})
export abstract class CardCollectionComponent implements OnInit {

  // @Input protected cards: CardCollection;

  constructor(@Inject('cards') protected cards: CardCollection) {}
  // constructor(@Inject('cards') protected cards: CardCollection) {}

  ngOnInit() {}
}
