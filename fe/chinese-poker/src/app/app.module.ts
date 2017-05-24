import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { Deck } from './deck/deck';
import { AppComponent } from './app.component';
import { CardComponent } from './card/card.component';
import { DeckComponent } from './deck/deck.component';

@NgModule({
  declarations: [
  AppComponent,
  CardComponent,
  DeckComponent,
  ],
  imports: [
  BrowserModule,
  FormsModule,
  HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
