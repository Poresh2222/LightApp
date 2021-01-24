import { Component, OnInit, Input } from '@angular/core';

import { BaseComponent } from '../base/base.component';

@Component({
  selector: 'app-base-page',
  templateUrl: './base-page.component.html',
  styleUrls: ['./base-page.component.scss']
})
export class BasePageComponent extends BaseComponent {

  protected _data:any;

  @Input()
  set data(dataInput: any) {
    this._data = dataInput
  }

  get data(): any { return this._data }

  constructor() { super() }

  ngOnInit(): void {
  }

}

export type ConfirmationResponse = {
  isConfirmed: boolean;
  data: any;
}

@Component({
  template: '',
}) 
export class BasePageComponentWithDialogs extends BasePageComponent {

}
