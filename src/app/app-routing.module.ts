import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent } from './pages/about/about.component';
import { ActivitiesComponent } from './pages/activities/activities.component';
import { BlogComponent } from './pages/blog/blog.component';
import { CastingComponent } from './pages/casting/casting.component';
import { ContactComponent } from './pages/contact/contact.component';
import { HomeComponent } from './pages/home/home.component';
import { NotFoundComponent } from './pages/not-found/not-found.component';

const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'sobre', component: AboutComponent },
  {
    path: 'casting',
    children: [
      {
        path: 'talentos',
        component: CastingComponent
      },
      {
        path: 'exclusivos',
        component: CastingComponent
      },
      {
        path: 'atores',
        component: CastingComponent
      },
      {
        path: 'infantil',
        component: CastingComponent
      }
    ]
  },
  { path: 'blog', component: BlogComponent },
  { path: 'contato', component: ContactComponent },
  { path: 'servicos', component: ActivitiesComponent },
  { path: 'home', component: HomeComponent },

  { path: '404', component: NotFoundComponent },
  { path: '**', component: NotFoundComponent }
];

@NgModule({
  imports: [
    CommonModule,
    BrowserModule,
    RouterModule.forRoot(routes, {
      useHash: false
    })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
