import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CastingComponent } from './casting/casting.component';
import { NewsComponent } from './news/news.component';
import { AboutComponent } from './about/about.component';
import { ActivitiesComponent } from './activities/activities.component';

@NgModule({
  declarations: [
    CastingComponent,
    NewsComponent,
    AboutComponent,
    ActivitiesComponent
  ],
  imports: [CommonModule]
})
export class AdminModule {}
