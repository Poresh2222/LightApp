import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { BasePageComponent } from './components/base-page/base-page.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent extends BasePageComponent {
  title = 'client';

  constructor(
    public router: Router
  ) { super() }

  ngOnInit(): void {
    this.router.navigate(['startpage'])
  }

}
