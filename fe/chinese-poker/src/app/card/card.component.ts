import { Component, Input, OnInit } from '@angular/core';
import { Card } from './card';
@Component({
  selector: 'card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css']
})
export class CardComponent {
  @Input() card: Card;
}
