import { Component, OnInit } from '@angular/core';
import { MatDialog, MatDialogModule, MatDialogRef } from '@angular/material/dialog';
import { Router } from '@angular/router';

import { BasePageComponent } from '../../base-page/base-page.component'


@Component({
  template: ''
})
export class SingupRouteComponent implements OnInit {

  constructor(
    public dialog: MatDialog,
    public router: Router
    ) { }

  ngOnInit(): void {
    this.openDialog()
  }

  openDialog() {
    const dialogRef = this.dialog.open(SingupComponentDialog);

    dialogRef.afterClosed().subscribe(result => {
      this.router.navigate(['startpage'])
    })
  }

}
@Component({
  selector: 'app-singup-dialog',
  templateUrl: './singup.component.html',
})
export class SingupComponentDialog extends BasePageComponent{

  constructor(public dialogRef: MatDialogRef<SingupComponentDialog>) {
    super()
  }

  closeDialog() {
    this.dialogRef.close()
  }

}