import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SingupRouteComponent } from './components/dialog/singup/singup.component';

const routes: Routes = [
  {path: 'singup', component: SingupRouteComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
