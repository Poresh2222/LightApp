import { Component, OnInit } from '@angular/core';

import { BasePageComponent } from '../base-page/base-page.component';

@Component({
  selector: 'app-start-page',
  templateUrl: './start-page.component.html',
  styleUrls: ['./start-page.component.scss']
})
export class StartPageComponent extends BasePageComponent {

  constructor() { super()}

  ngOnInit(): void {
  }

}
