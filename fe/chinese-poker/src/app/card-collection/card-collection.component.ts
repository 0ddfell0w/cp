import { Component, OnInit } from '@angular/core';
import { Card } from '../card/card';

@Component({
  selector: 'app-card-collection',
  templateUrl: './card-collection.component.html',
  styleUrls: ['./card-collection.component.css']
})
export abstract class CardCollectionComponent implements OnInit {

  constructor(protected cards: Array<Card>) {}

  ngOnInit() {
  }
}
