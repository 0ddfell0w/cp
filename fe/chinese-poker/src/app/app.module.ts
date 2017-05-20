import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { CardComponent } from './card/card.component';
import { DeckComponent } from './deck/deck.component';
import { CardCollectionComponent } from './card-collection/card-collection.component';

@NgModule({
  declarations: [
  AppComponent,
  CardComponent,
  DeckComponent,
  CardCollectionComponent,
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
