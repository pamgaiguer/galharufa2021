import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { AboutComponent } from './about/about.component';
import { CastingComponent } from './casting/casting.component';
import { ContactComponent } from './contact/contact.component';
import { ServicesComponent } from './services/services.component';
import { HomeComponent } from './home/home.component';
import { NotFoundComponent } from './not-found/not-found.component';

@NgModule({
  declarations: [
    AboutComponent,
    ServicesComponent,
    CastingComponent,
    ContactComponent,
    HomeComponent,
    NotFoundComponent,
  ],
  imports: [CommonModule],
})
export class PagesModule {}
