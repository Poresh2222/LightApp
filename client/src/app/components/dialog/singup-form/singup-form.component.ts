import { Component, OnInit, AfterViewInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { BasePageComponent } from '../../base-page/base-page.component'
import { SingupComponentDialog } from '../singup/singup.component';


@Component({
  selector: 'singup-form',
  templateUrl: './singup-form.component.html',
  styleUrls: ['./singup-form.component.scss']
})
export class SingupFormComponent extends BasePageComponent implements AfterViewInit {
  firstFormGroup: FormGroup;
  secondFormGroup: FormGroup;
  isEditable = false;

  constructor(
    private _formBuilder: FormBuilder,
  )
  {super() }

  ngOnInit() {
    this.firstFormGroup = this._formBuilder.group({
      firstCtrl: ['', Validators.required]
    });
    this.secondFormGroup = this._formBuilder.group({
      secondCtrl: ['', Validators.required]
    });
  }

  ngAfterViewInit(): void {

  }

}
