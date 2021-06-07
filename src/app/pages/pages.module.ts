import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { AboutComponent } from './about/about.component';
import { CastingComponent } from './casting/casting.component';
import { ContactComponent } from './contact/contact.component';
import { ServicesComponent } from './services/services.component';

@NgModule({
  declarations: [
    AboutComponent,
    ServicesComponent,
    CastingComponent,
    ContactComponent,
  ],
  imports: [CommonModule],
})
export class PagesModule {}
