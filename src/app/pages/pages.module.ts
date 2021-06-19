import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AboutComponent } from './about/about.component';
import { ActivitiesComponent } from './activities/activities.component';
import { CastingComponent } from './casting/casting.component';
import { ContactComponent } from './contact/contact.component';
import { HomeComponent } from './home/home.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { BlogComponent } from './blog/blog.component';

@NgModule({
  declarations: [AboutComponent, ActivitiesComponent, CastingComponent, ContactComponent, HomeComponent, NotFoundComponent, BlogComponent],
  imports: [CommonModule, NgbModule],
  exports: [NgbModule]
})
export class PagesModule {}
