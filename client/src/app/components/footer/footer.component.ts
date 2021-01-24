import { Component, OnInit } from '@angular/core';

import { BasePageComponent } from '../base-page/base-page.component';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent extends BasePageComponent {

  constructor() { super() }

  ngOnInit(): void {
  }

}
