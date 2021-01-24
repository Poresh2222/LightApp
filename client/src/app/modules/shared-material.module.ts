import { NgModule } from '@angular/core';
import { MatSliderModule } from '@angular/material/slider';
import { MatMenuModule }  from '@angular/material/menu';
import { MatToolbarModule } from '@angular/material/toolbar'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonModule } from '@angular/material/button';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatListModule } from '@angular/material/list';
import { MatDialogModule } from '@angular/material/dialog';
import { MatStepperModule}  from '@angular/material/stepper';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';


const SharedMaterialComponents = [
    MatSliderModule,
    MatMenuModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    MatGridListModule,
    MatListModule,
    MatDialogModule,
    MatStepperModule,
    MatFormFieldModule,
    MatInputModule,
]

@NgModule({
    imports: [SharedMaterialComponents],
    exports: [SharedMaterialComponents]
})

export class SharedMaterialModule { }