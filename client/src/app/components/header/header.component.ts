import { Component, OnInit } from '@angular/core';

import { SingupRouteComponent, SingupComponentDialog } from '../dialog/singup/singup.component';
import { BasePageComponent } from '../base-page/base-page.component';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent extends BasePageComponent {

  constructor(
   ) { super()}

  ngOnInit(): void {

  }

}
