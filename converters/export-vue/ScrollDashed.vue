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
    <path d="m6,9v-4c0-1.1-.9-2-2-2s-2,.9-2,2v3h4" /><path d="m6,15v-2" /><path d="m20,21h0c1.1,0,2-.9,2-2v-2h-12v2c0,1.1-.9,2-2,2s-2-.9-2-2h0" /><path d="m15,21h1" /><path d="m8,21h3" /><path d="m7,3h-3" /><path d="m14,3h-3" /><path d="m20,5h0c0-1.1-.9-2-2-2h0" /><path d="m20,11v-2" /><path d="m20,17v-2" />
  </svg>
</template>

<script setup>
  const props = defineProps({
    size: { type: [String, Number], default: 24 },
    stroke: { type: [String, Number], default: 1.5 },
  });
</script>

<style lang="scss" scoped></style>