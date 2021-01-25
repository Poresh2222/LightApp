import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SingupRouteComponent } from './components/dialog/singup/singup.component';
import { StartPageComponent } from './components/start-page/start-page.component';
import { SingInRouteComponent } from './components/dialog/singin/singin.component';
import { HomePageComponent } from './components/home-page/home-page.component';

const routes: Routes = [
  {path: 'startpage', component: StartPageComponent},
  {path: 'singup', component: SingupRouteComponent},
  {path: 'singin', component: SingInRouteComponent},
  {path: 'home', component: HomePageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
