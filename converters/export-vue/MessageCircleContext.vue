<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    :stroke-width="stroke"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path d="m3.85,15.38c-1.87-1.18-2.42-3.65-1.24-5.52.32-.5.74-.92,1.24-1.24-.48-2.16.88-4.29,3.04-4.77.57-.13,1.17-.13,1.74,0,1.19-1.86,3.66-2.41,5.52-1.22.49.31.9.73,1.22,1.22,2.16-.48,4.3.87,4.78,3.03.13.58.13,1.18,0,1.75,1.86,1.19,2.41,3.66,1.22,5.52-.31.49-.73.9-1.22,1.22.48,2.16-.87,4.29-3.03,4.78-.57.13-1.17.13-1.74,0-1.19,1.86-3.66,2.41-5.52,1.23-.49-.31-.91-.73-1.23-1.23l-.74-.15-5.9,2,2.01-6-.15-.62Z" />
  </svg>
</template>

<script setup>
  const props = defineProps({
    size: { type: [String, Number], default: 24 },
    stroke: { type: [String, Number], default: 1.5 },
  });
</script>

<style lang="scss" scoped></style>