import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AboutComponent } from './about/about.component';
import { CastingComponent } from './casting/casting.component';
import { ContactComponent } from './contact/contact.component';
import { HomeComponent } from './home/home.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { ServicesComponent } from './services/services.component';

@NgModule({
  declarations: [
    AboutComponent,
    ServicesComponent,
    CastingComponent,
    ContactComponent,
    HomeComponent,
    NotFoundComponent,
  ],
  imports: [CommonModule, NgbModule],
})
export class PagesModule {}
