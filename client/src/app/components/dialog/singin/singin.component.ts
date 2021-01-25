import { Component, OnInit } from '@angular/core';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { BasePageComponent } from '../../base-page/base-page.component'


@Component({
  template: ''
})
export class SingInRouteComponent implements OnInit {
  LoginStatus = true;

  constructor(
    public dialog: MatDialog,
    public router: Router
    ) { }

  ngOnInit(): void {
    this.openDialog()
  }

  openDialog() {
    const dialogRef = this.dialog.open(SinginComponent);

    dialogRef.afterClosed().subscribe(result => {
      if (this.LoginStatus == false) {
        this.router.navigate(['startpage'])
      }
      else {
        this.router.navigate(['home'])
      }
    })
  }

}
@Component({
  selector: 'app-singin',
  templateUrl: './singin.component.html',
  styleUrls: ['./singin.component.scss']
})
export class SinginComponent extends BasePageComponent {
  loginFormGroup: FormGroup;

  constructor(
    public dialogRef: MatDialogRef<SinginComponent>,
    private _formBuilder: FormBuilder
  ) { super() }

  closeDialog() {
    this.dialogRef.close()
  }

  ngOnInit() {
    this.loginFormGroup = this._formBuilder.group({
      loginCtrl: ['', Validators.required]
    })
  }


}
