# Proyecto Sistema de Reservas con Integración UML

**Enlace al repositorio en GitHub:** [https://github.com/pramos-m/proyecto-uml-reservas](https://github.com/pramos-m/proyecto-uml-reservas)

Este repositorio contiene el código fuente para un sistema de reservas simple y los diagramas UML asociados que documentan su diseño. El objetivo es mantener una sincronización entre el diseño (UML) y la implementación (Python).

##  आर्किटेक्चर

El sistema está compuesto por las siguientes clases principales:
- `Usuario`: Representa a un usuario que puede hacer reservas.
- `Sala`: Representa una sala que puede ser reservada.
- `Reserva`: Representa la acción de reservar una sala por un usuario en un horario específico.

Los diagramas UML se encuentran en la carpeta `/diagrams`. Actualmente utilizamos PlantUML para la generación de diagramas a partir de texto.

## 📜 Normas para actualizar el UML [cite: 24]

1.  **Diseño Primero (para nuevas funcionalidades significativas):**
    * Antes de implementar una nueva funcionalidad compleja o realizar cambios estructurales mayores (ej. añadir nuevas clases, cambiar relaciones fundamentales), el diagrama UML de clases debe ser actualizado o creado primero.
    * Discutir los cambios en el diseño con el equipo si es necesario.

2.  **Actualización Post-Implementación (para refactorizaciones o cambios menores):**
    * Si se realizan refactorizaciones que alteran la estructura de las clases (ej. renombrar métodos/atributos importantes, cambiar signaturas, modificar relaciones) o se añaden/eliminan clases/métodos/atributos, el diagrama UML debe actualizarse para reflejar estos cambios *después* de que el código haya sido probado y esté estable.

3.  **Consistencia Obligatoria:** El diagrama UML y el código deben estar sincronizados antes de fusionar cualquier rama de funcionalidad (`feature branch`) a la rama principal (`main` o `develop`).

4.  **Formato de Diagramas:**
    * Los diagramas UML de clases se mantendrán como archivos de texto PlantUML (extensión `.puml`). [cite: 29]
    * Se pueden incluir imágenes exportadas (ej. `.png`) de los diagramas en la carpeta `/diagrams/generated` para fácil visualización, pero el archivo `.puml` es la fuente de verdad.

5.  **Revisión de Cambios UML:** Los cambios en los archivos `.puml` deben ser parte de las revisiones de código (Pull Requests).

## ✨ Buenas prácticas para commit de cambios [cite: 25]

1.  **Commits Atómicos:** Realiza commits pequeños y lógicos. Si un cambio afecta tanto al código como al UML, idealmente se commitean juntos o en commits muy cercanos con mensajes claros.
    * Ejemplo: Si añades una nueva clase y su respectivo diagrama: `git commit -m "feat: Add Payment class and UML diagram"`
2.  **Mensajes de Commit Descriptivos:** [cite: 30]
    * Utiliza el formato de commits convencionales si es posible (ej. `feat:`, `fix:`, `docs:`, `refactor:`, `style:`).
    * Si actualizas el UML, indícalo claramente.
        * `docs(UML): Update class diagram to reflect new User properties`
        * `refactor: Rename Sala.get_availability to Sala.esta_disponible and update UML`
3.  **Incluir Archivos UML:** Asegúrate de que los archivos `.puml` (y las imágenes generadas, si se decide versionarlas) se añadan y commiteen al repositorio.
4.  **Ramas para Cambios:** Utiliza ramas separadas para nuevas funcionalidades o correcciones de errores. [cite: 28] No trabajes directamente sobre la rama principal.
    * Ej: `feature/user-profile`, `fix/reservation-bug`

## 🔄 Ejemplo de ciclo: diseño → código → actualización UML [cite: 25]

**Escenario:** Añadir la capacidad de que un `Usuario` tenga un `tipo` (ej. "Estudiante", "Profesor").

1.  **Diseño (Actualización UML):**
    * Crear/checkout una nueva rama: `git checkout -b feature/user-type`
    * Modificar el archivo `diagrams/class_diagram.puml` para añadir el atributo `tipo: String` a la clase `Usuario`.
    * Generar la imagen del diagrama si es necesario.
    * `git add diagrams/class_diagram.puml diagrams/generated/class_diagram.png`
    * `git commit -m "docs(UML): Add 'tipo' attribute to Usuario class"`

2.  **Código (Implementación):**
    * Modificar la clase `Usuario` en el archivo Python para incluir el nuevo atributo `tipo` en el `__init__` y como propiedad.
    * Añadir pruebas unitarias si aplica.
    * `git add src/usuario.py tests/test_usuario.py`
    * `git commit -m "feat: Implement 'tipo' attribute for Usuario class"`

3.  **Revisión y Fusión:**
    * Crear un Pull Request de `feature/user-type` a `main` (o `develop`).
    * El equipo revisa que el código y el UML sean consistentes.
    * Fusionar el Pull Request.

## 🗂️ Estructura del Repositorio (Ejemplo)